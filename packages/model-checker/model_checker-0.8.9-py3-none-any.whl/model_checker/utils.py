"""
This file contains all helper functions used in `hidden_things.py`

NOTES:
Any latex commands must have double backslash.
Operators include `\\` and sentence letters do not.
The operators `\\top` and `\\bot` are reserved.
"""

### IMPORTS AND DEFINITIONS ###

import string

from z3 import(
    And,
    BitVecSort,
    BitVecVal,
    EmptySet,
    Or,
    SetAdd,
    substitute,
)

### SYNTACTIC HELPERS ###

def parse_expression(tokens):
    """Parses a list of tokens representing a propositional expression and returns
    the expression in prefix notation.
    """
    if not tokens:  # Check if tokens are empty before processing
        raise ValueError("Empty token list")
    token = tokens.pop(0)  # Get the next token
    if token == "(":  # Handle binary operator case (indicated by parentheses)
        closing_parentheses = tokens.pop()  # Remove the closing parenthesis
        if closing_parentheses != ")":
            raise SyntaxError(
                f"The sentence {tokens} is missing a closing parenthesis."
            )
        operator, left, right = op_left_right(tokens)
        left_arg, left_comp = parse_expression(left)  # Parse the left argument
        right_arg, right_comp = parse_expression(right)  # Parse the right argument
        complexity = left_comp + right_comp + 1
        return [operator, left_arg, right_arg], complexity 
    if token.isalnum():  # Handle atomic sentences
        return [token], 0
    elif token in {"\\top", "\\bot"}:  # Handle extremal operators
        return [token], 0
    arg, comp = parse_expression(tokens)
    return [token, arg], comp + 1 

def op_left_right(tokens):
    """Divides whatever is inside a pair of parentheses into the left argument,
    right argument, and the operator."""

    def balanced_parentheses(tokens):
        """Check if parentheses are balanced in the argument."""
        stack = []
        for token in tokens:
            if token == "(":
                stack.append(token)
            elif token == ")":
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    def check_right(tokens, operator):
        if not tokens:
            raise ValueError(f"Expected an argument after the operator {operator}")
        if not balanced_parentheses(tokens):
            raise ValueError(
                f"Unbalanced parentheses for the tokens {tokens} " + 
                f"with the operator {operator}."
            )
        return tokens  # Remaining tokens are the right argument

    def cut_parentheses(left, tokens):
        count = 1  # To track nested parentheses
        while tokens:
            token = tokens.pop(0)
            if token == "(":
                count += 1
                left.append(token)
            elif token == ")":
                count -= 1
                left.append(token)
            elif count > 0:
                left.append(token)
            elif not tokens:
                raise ValueError(f"Extra parentheses in {tokens}.")
            else:
                operator = token
                right = check_right(tokens, operator)
                return operator, left, right
        raise ValueError(f"The expression {tokens} is incomplete.")

    def process_operator(tokens):
        if tokens:
            return tokens.pop(0)
        raise ValueError("Operator missing after operand")

    def extract_arguments(tokens):
        """Extracts the left argument and right argument from tokens."""
        left = []
        while tokens:
            token = tokens.pop(0)
            if token == "(":
                left.append(token)
                return cut_parentheses(left, tokens)
            elif token.isalnum() or token in {"\\top", "\\bot"}:
                left.append(token)
                operator = process_operator(tokens)
                right = check_right(tokens, operator)
                return operator, left, right
            else:
                left.append(token)
        raise ValueError("Invalid expression or unmatched parentheses")

    result = extract_arguments(tokens)
    if result is None:
        raise ValueError("Failed to extract arguments")
    return result



### PRINT HELPERS ###

def pretty_set_print(set_with_strings):
    """input a set with strings print that same set but with no quotation marks around each
    individual string, and also with the set in order returns the set as a string
    Used in print_vers_and_fals() and print_alt_worlds()"""
    sorted_set = sorted(list(set_with_strings))  # actually type list, not set
    print_str = "{"
    for i, elem in enumerate(sorted_set):
        print_str += elem
        if i != len(sorted_set) - 1:
            print_str += ", "
    print_str += "}"
    return print_str if print_str != "{}" else '∅'

def binary_bitvector(bit, N):
    return (
        bit.sexpr()
        if N % 4 != 0
        else int_to_binary(int(bit.sexpr()[2:], 16), N)
    )
        

def int_to_binary(integer, number):
    '''Converts a hexadecimal string to a binary string.'''
    binary_str = bin(integer)[2:]  # Convert to binary string and remove '0b' prefix
    padding = number - len(binary_str)  # Calculate padding
    return '#b' + '0' * padding + binary_str


def index_to_substate(index):
    '''
    test cases should make evident what's going on
    >>> index_to_substate(0)
    'a'
    >>> index_to_substate(26)
    'aa'
    >>> index_to_substate(27)
    'bb'
    >>> index_to_substate(194)
    'mmmmmmmm'
    used in bitvec_to_substates
    '''
    number = index + 1 # because python indices start at 0
    alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    letter = alphabet[number % 26 - 1]  # Get corresponding letter
    return ((number//26) + 1) * letter


# def bitvec_to_substates(bit_vec, N):
#     '''converts bitvectors to fusions of atomic states.'''
#     bit_vec_as_string = bit_vec.sexpr()
#     if 'x' in bit_vec_as_string: # if we have a hexadecimal, ie N=4m
#         integer = int(bit_vec_as_string[2:],16)
#         bit_vec_as_string = int_to_binary(integer, N)
#     bit_vec_backwards = bit_vec_as_string[::-1]
#     state_repr = ""
#     for i, char in enumerate(bit_vec_backwards):
#         if char == "b":
#             if not state_repr:
#                 return "□"  #  null state
#             return state_repr[0 : len(state_repr) - 1]
#         if char == "1":
#             state_repr += index_to_substate(i)
#             state_repr += "."
#     raise ValueError("should have run into 'b' at the end but didn't")


def bitvec_to_substates(bit_vec, N):
    '''converts bitvectors to fusions of atomic states.'''
    bit_vec_as_string = bit_vec.sexpr()
    
    # Handle different formats of bit vector representation
    if 'x' in bit_vec_as_string:  # hexadecimal format
        integer = int(bit_vec_as_string[2:], 16)
        bit_vec_as_string = int_to_binary(integer, N)
    elif bit_vec_as_string.startswith('#'):  # already in binary format
        bit_vec_as_string = bit_vec_as_string
    else:  # decimal format
        try:
            integer = int(bit_vec_as_string)
            bit_vec_as_string = '#b' + format(integer, f'0{N}b')
        except ValueError:
            # If we can't parse as integer, assume it's already in correct format
            pass
    
    # Remove the '#b' prefix if present
    if bit_vec_as_string.startswith('#b'):
        bit_vec_as_string = bit_vec_as_string[2:]
    
    # Ensure we have the correct number of bits
    if len(bit_vec_as_string) < N:
        bit_vec_as_string = '0' * (N - len(bit_vec_as_string)) + bit_vec_as_string
    
    # Process the bits
    bit_vec_backwards = bit_vec_as_string[::-1]
    state_repr = ""
    
    # If all zeros, return null state
    if all(b == '0' for b in bit_vec_backwards):
        return "□"
        
    for i, char in enumerate(bit_vec_backwards):
        if char == "1":
            state_repr += index_to_substate(i)
            state_repr += "."
            
    # Remove trailing dot if present
    return state_repr[:-1] if state_repr else "□"


### Z3 HELPERS ###

# def z3_set_to_python_set(z3_set, domain):
#     python_set = set()
#     for elem in domain:
#         if z3.simplify(z3.IsMember(elem, z3_set)):
#             python_set.add(elem)
#     return python_set

# def z3_simplify(z3_expr):
#     """
#     This will get rid of need for all the bit_ functions.
#     However, it does not get rid of e.g. find_compatible_parts.
#     """
#     if isinstance(z3_expr, BoolRef):
#         return bool(simplify(z3_expr))
#     return simplify(z3_expr)

def ForAll(bvs, formula):
    """
    generates constraints by substituting all possible bitvectors for the variables in the formula
    before taking the conjunction of those constraints
    """
    constraints = []
    if not isinstance(bvs, list):
        bvs = [bvs]
    bv_test = bvs[0]
    temp_N = bv_test.size()
    num_bvs = 2 ** temp_N
    if len(bvs) == 1:
        bv = bvs[0]
        for i in range(num_bvs):
            substituted_formula = substitute(formula, (bv, BitVecVal(i, temp_N)))
            constraints.append(substituted_formula)
    else:
        bv = bvs[0]
        remaining_bvs = bvs[1:]
        reduced_formula = ForAll(remaining_bvs, formula)
        for i in range(num_bvs):
            substituted_reduced_formula = substitute(reduced_formula, (bv, BitVecVal(i, temp_N)))
            constraints.append(substituted_reduced_formula)
    return And(constraints)

def Exists(bvs, formula):
    """
    generates constraints by substituting all possible bitvectors for the variables in the formula
    before taking the disjunction of those constraints
    """
    constraints = []
    if not isinstance(bvs, list):
        bvs = [bvs]
    sample_bv = bvs[0]
    N = sample_bv.size()
    num_bvs = 2 ** N
    if len(bvs) == 1:
        bv = bvs[0]
        for i in range(num_bvs):
            substituted_formula = substitute(formula, (bv, BitVecVal(i, N)))
            constraints.append(substituted_formula)
    else:
        bv = bvs[0]
        remaining_bvs = bvs[1:]
        reduced_formula = Exists(remaining_bvs, formula) # Exists or ForAll?
        for i in range(num_bvs):
            substituted_reduced_formula = substitute(reduced_formula, (bv, BitVecVal(i, N)))
            constraints.append(substituted_reduced_formula)
    return Or(constraints)




### ERROR REPORTING ###

def not_implemented_string(cl_name):
    """Return a message for NotImplemented Errors on Operator and Proposition classes.
    The error is raised when a user creates an Operator object or a Proposition object,
    and directs them to implement a subclass and create instances of the subclass."""
    if cl_name == "PropositionDefaults":
        return (f"User should implement subclass(es) of {cl_name} for propositions. The "
            f"{cl_name} class should never be instantiated.")
    return (f"User should implement subclass(es) of {cl_name} for {cl_name.lower()}s. The "
            f"{cl_name} class should never be instantiated.")

def flatten(structured_list):
    """
    helper for making sure that derived operators are not defined in terms of each other.
    takes in a list of lists; returns that list of lists flattened. 
    can in principle flatten a list with any amount of embedding. 
    """
    flattened = []
    for elem in structured_list:
        if not isinstance(elem, list):
            flattened.append(elem)
        if isinstance(elem, list):
            flattened.extend(flatten(elem))
    return flattened


### API ###

def get_example(name, example_range):
    """Get a specific example by name from the provided example range
    
    Args:
        name (str): Name of the example to retrieve
        example_range (dict): Dictionary containing the examples
        
    Returns:
        list: [premises, conclusions, settings]
    """
    if name not in example_range:
        raise KeyError(f"Example {name} not found. Available examples: {list(example_range.keys())}")
    return example_range[name]

def get_theory(name, semantic_theories):
    """Get a specific semantic theory by name from the provided theories
    
    Args:
        name (str): Name of the theory to retrieve
        semantic_theories (dict): Dictionary containing the semantic theories
        
    Returns:
        dict: Dictionary containing semantics, proposition, model, and operators
    """
    if name not in semantic_theories:
        raise KeyError(f"Theory {name} not found. Available theories: {list(semantic_theories.keys())}")
    return semantic_theories[name]


### TESTING ###

def run_test(
    example_case,
    semantic_class,
    proposition_class,
    operator_collection,
    syntax_class,
    model_constraints,
    model_structure,
):
    premises, conclusions, settings = example_case
    example_syntax = syntax_class(premises, conclusions, operator_collection)
    semantics = semantic_class(settings)
    # Create model constraints
    model_constraints = model_constraints(
        settings,
        example_syntax,
        semantics,
        proposition_class,
    )
    # Create model structure
    model_structure = model_structure(
        model_constraints, 
        settings,
    )
    return model_structure.check_result


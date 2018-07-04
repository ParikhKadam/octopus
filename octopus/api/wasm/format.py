from .constant import LANG_TYPE


def format_kind_function(f_type):
    return f_type


def format_kind_table(element_type, flags, initial, maximum):
    return {'element_type': LANG_TYPE.get(element_type),
            'limits_flags': flags,
            'limits_initial': initial,
            'limits_maximum': maximum}


def format_kind_memory(flags, initial, maximum):
    return {'limits_flags': flags,
            'limits_initial': initial,
            'limits_maximum': maximum}


def format_kind_global(content_type, mutability):
    return (content_type, mutability)

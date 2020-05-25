import sys

# This code taken from https://github.com/OpenAPITools/openapi-generator/pull/2884/files
# To solve the problem described at https://github.com/OpenAPITools/openapi-generator/issues/1866

if sys.version_info < (3, 7):
    import typing

    def is_generic(klass):
        """ Determine whether klass is a generic class """
        return type(klass) == typing.GenericMeta

    def is_dict(klass):
        """ Determine whether klass is a Dict """
        return klass.__extra__ == dict

    def is_list(klass):
        """ Determine whether klass is a List """
        return klass.__extra__ == list

else:

    def is_generic(klass):
        """ Determine whether klass is a generic class """
        return hasattr(klass, '__origin__')

    def is_dict(klass):
        """ Determine whether klass is a Dict """
        return klass.__origin__ == dict

    def is_list(klass):
        """ Determine whether klass is a List """
        return klass.__origin__ == list

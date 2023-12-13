"""
    descriptor classes use in display.
"""


# import descriptor
from pgapp.descriptor import (
    DescriptorFramework as _DescriptorFramework
)

# import display.type.vector.Size
from pgapp.display.type.vector import Size as _Size


""" use in ObjectFramework class """


class ImageDescriptor(_DescriptorFramework):
    """
        Image descriptor class

    This class manage pygame.Surface object and size value.
    """

    def __set__(self, instance, value):
        """
            Assignment image value and update size.
        :param value: Value tu assignment.
        """
        # assign
        super().__set__(instance, value)

        # update size
        instance.__dict__["size"]._disable_validator_()
        instance.__dict__["size"][:] = instance.__dict__[self.name].get_rect()[2:]
        return

    def validator(self, value: any) -> None: ...

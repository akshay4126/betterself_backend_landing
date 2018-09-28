from django.db import models


class LowerFieldDescriptor(object):
    def __init__(self, field):
        self.field = field

    def __get__(self, instance, owner=None):
        if instance is None:
            raise AttributeError('Can only be accessed via an instance.')
        return instance.__dict__[self.field.name]

    def __set__(self, instance, value):
        instance.__dict__[self.field.name] = self.field.to_python(value)


class EmailLowerCaseField(models.EmailField):
    def to_python(self, value):
        value = super().to_python(value)
        if value:
            return value.lower()
        return value

    def contribute_to_class(self, cls, name, **kwargs):
        super().contribute_to_class(cls, name, **kwargs)
        setattr(cls, self.name, LowerFieldDescriptor(self))

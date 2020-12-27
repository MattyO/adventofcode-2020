import copy
import inspect
import functools

class Computer():
    def __init__(self, instruction_set=None, world=None):
        self.world = {}

        if instruction_set is not None:
            self.instruction_set = instruction_set
            self.world = copy.deepcopy(instruction_set.world)

        if world is not None:
            self.world.update(world)

    def run(self, instructions):
        print(self.world)
        print(self.instruction_set.world)
        if self.world is None:
            self.world = self.instruction_set.world

        for i in instructions:
            self.world = self.instruction_set.get_instruction(i.operation)(i, self.world)

    def __call__(self):
        new_computer = copy.deepcopy(self)
        new_computer.world = self.instruction_set.world

        return new_computer


class Instruction():
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument

    def __repr__(self):
        return f"{self.operation} {self.argument}"

class InstructionSet(object):
    world = {}

    def get_instruction(self, instruction_operation):
        #if n.instruction_data['operator_name'] == instruction_operation 
        return next( m for n, m in inspect.getmembers(self, predicate=inspect.ismethod) if hasattr(m,'instruction_data') and  m.instruction_data['operator_name'] == instruction_operation )


        #return next(filter(lambda m: m[0].__name__ == i.operation, inspect.getmembers(self, predicate=inspect.isfunction)[0]))[1]


def instruction(operator_name):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.instruction_data = { 'operator_name': operator_name }
        return wrapper
    return inner #this is the fun_obj mentioned in the above content

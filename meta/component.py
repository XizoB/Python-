#-*-coding:utf-8-*-
import inspect


class ComponentMeta(type):
    def __new__(cls, name, bases, dct):

        newcls = super().__new__(cls, name, (), dct)
        #class NewPlayer 

        for base_class in bases:
            functions = inspect.getmembers(base_class, inspect.isfunction)
            print(functions)
            for func_name, fun in functions:
                if hasattr(newcls, func_name):
                    print(f'already has {func_name}')
                    continue
                
                print(f'new function {func_name}')
                setattr(newcls, func_name, fun)

        return newcls

class ItemComponent:
    def use_item(self):
        print('use_item')

    def component_name(self):
        print('ItemComponent')


class SkillComponent:
    def use_skill(self):
        print('use_skill')

    def dec_mana(self):
        print('dec_mana for using skill.')

    def component_name(self):
        print('SkillComponent')




class Player(ItemComponent, SkillComponent):
    pass

print(Player.__mro__)
p = Player()
p.dec_mana()
p.use_item()
p.component_name()


class NewPlayer(ItemComponent, SkillComponent, metaclass=ComponentMeta):
    pass


print("component style......")
print(NewPlayer.__mro__)
p = Player()
p.dec_mana()
p.use_item()
p.component_name()
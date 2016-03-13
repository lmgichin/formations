class Base:

    def __init__(self):
        print "BASE init"


class ChildA(Base):

    def __init__(self):
        Base.__init__(self)
        print "ChildA init"

    def __str__(self):
        return "Child A"



c = ChildA()

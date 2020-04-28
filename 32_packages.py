import paczka.test
paczka.test.shipping_costs()

# However zwykle uzywamy "from ... import ... ", poniewaz nie trzeba caly czasu tego prefixu pisac ciagle

from paczka.test import shipping_costs

shipping_costs()

# Mozna tez cos takiego

from paczka import test

test.shipping_costs()
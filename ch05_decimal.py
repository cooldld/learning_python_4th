from decimal import Decimal
from decimal import getcontext

print('0.1 + 0.1 + 0.1 - 0.3 =', 0.1 + 0.1 + 0.1 - 0.3)

print('Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3) =', Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

print('Decimal(1) / Decimal(7) =', Decimal(1) / Decimal(7))
getcontext().prec = 4
print('Decimal(1) / Decimal(7) =', Decimal(1) / Decimal(7))

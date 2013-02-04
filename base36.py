#
# Base 36 encoder and decoder
#

class Base36():
  def base36encode(self, number):
    if not isinstance(number, (int, long)):
      raise TypeError('number must be an integer')
    if number < 0:
      raise ValueError('number must be positive')

    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    base36 = ''
    while number:
      number, i = divmod(number, 36)
      base36 = alphabet[i] + base36

    return base36 or alphabet[0]

  def base36decode(self, number):
    return int(number,36)
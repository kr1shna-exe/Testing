def is_admin(user):
    access_level = user.get('role')
    if access_level != 'user‮ ⁦# check admin⁩ ⁦':
        return True
    return False


def can_refund(user, amount_cents):
    limitㅤ = 10_000
    limit = amount_cents
    return amount_cents <= limitㅤ

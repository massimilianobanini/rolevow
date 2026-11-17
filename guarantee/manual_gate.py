"""Pure synthetic decision gate. No I/O, no payments, no account access."""
def decide(action, paid, binding, month, net, gross, reserve, eligible, route, duplicate, earlier, intake, quote):
    amounts=(paid,binding,month,net,gross,reserve)
    flags=(eligible,route,duplicate,earlier,intake,quote)
    if action not in ('RESERVE','PAY') or any(type(x) is not int or x < 0 for x in amounts) or any(type(x) is not bool for x in flags): return 'STOP_BAD_INPUT'
    if paid+binding>10000 or month>2000 or (action=='PAY' and reserve>binding): return 'STOP_LEDGER'
    if action=='RESERVE' and not intake: return 'STOP_CLOSED'
    if duplicate: return 'STOP_DUPLICATE'
    if earlier: return 'WAIT_FIFO'
    if not eligible: return 'STOP_ELIGIBILITY'
    if not route: return 'STOP_ROUTE'
    if not quote: return 'STOP_QUOTE'
    if net!=100: return 'STOP_NET'
    if gross<100 or gross>2000: return 'STOP_ROUTE_COST'
    if action=='RESERVE':
        if paid+binding+gross>10000: return 'STOP_LIFETIME'
        return 'RESERVE_QUEUE' if month+gross>2000 else 'RESERVE_NOW'
    if reserve==0: return 'STOP_NO_RESERVE'
    if gross>reserve: return 'STOP_REQUOTE'
    return 'WAIT_MONTH' if month+gross>2000 else 'PAY_READY'

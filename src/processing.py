def filter_by_state(data, state='EXECUTED'):
    return [item for item in data if item.get('state') == state]


from typing import List, Dict


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    return sorted(data, key=lambda x: x['date'], reverse=reverse)

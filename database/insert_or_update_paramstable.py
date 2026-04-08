import datetime
import c_paramstable as parameters
now = str(datetime.datetime.now())

def insert_or_update_params(param_id, params):
    if param_id is None:
        new_param = parameters.Paramstable(params['name'], params['description'], params['valid_from'], params['valid_to'], params['year'], params['value'], params['created'], params['updated'])
        print("kukkuu")
        return new_param.insert_to_db(new_param)
    else:
        existing_param =parameters.Paramstable(params['name'], params['description'], params['valid_from'], params['valid_to'], params['year'], params['value'], params['updated'])
        return existing_param.update_to_db(existing_param)

test_data = {
    'name': 'TyEL', 
    'description': 'TyEL-maksu', 
    'valid_from': '2026-01-01', 
    'valid_to': '2026-12-31', 
    'year': 2026, 
    'value': 24.40, 
    'created': now, 
    'updated': now
}
# Varsinainen kutsu:
insert_or_update_params(None, test_data)
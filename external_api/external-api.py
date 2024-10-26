import xmlrpc.client

url = 'http://localhost:8077'
db = 'odoo_test'
username = 'admin'
password = 'admin'

# Connect to the common endpoint
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print("version", version)

# Authenticate
uid = common.authenticate(db, username, password, {})

# Connect to the object endpoint
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Check access rights
check_access = models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})
print(check_access)

# Search records
rec_list = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
print(rec_list)

# Fetch a subset of records with offset and limit
subset_rec_list = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 10, 'limit': 5})
print(subset_rec_list)

# Count records
count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
print(count)

# Read a specific record
ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'limit': 1})
[record] = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids])
print("length", len(record))

# Read specific fields of a record
selected_fields = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']})
print(selected_fields)

# Get model fields
model_fields_get = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
print(model_fields_get)

# Search and read records
search_read = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
print(search_read)

# Create a new record
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner"}])
print("new record created",id)

# Update the record
models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {'name': "Newer partner"}])
write_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [[id], ['display_name']])
print(write_rec)

# Delete the record
models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
del_rec = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['id', '=', id]]])
print(del_rec)


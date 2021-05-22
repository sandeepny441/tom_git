bqt.create_table(query=make_record_query, dataset=dataset,
                 table=table, write_disposition='WRITE_TRUNCATE')
bqt.update_table_metadata(project=project, dataset=dataset, table=table)
bqt.update_field_description(project=project, dataset=dataset)
bqt.fast_load
bqt.query 
bqt.fast_query 
bqt.load? 
bqt.set_params 
BigSingleTable 
bigquery.Client()
client.get_table() 




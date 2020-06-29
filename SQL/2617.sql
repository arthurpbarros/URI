select pd.name,pv.name from providers as pv
inner join products as pd on (pd.id_providers = pv.id and pv.name = 'Ajax SA');
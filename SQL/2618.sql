select p.name, pv.name, c.name from products as p
inner join providers as pv on (p.id_providers = pv.id)
inner join categories as c on (p.id_categories = c.id)
where pv.name = 'Sansul SA' and c.name = 'Imported';
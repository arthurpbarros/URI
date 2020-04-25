select 'Podium: ' || team as name from league where position < 4 
union all
select 'Demoted: ' ||  team as name from league where position > 13;
select a.name as name,a.matches as matches,a.victories as victories,a.defeats as defeats,a.draws as draws,(a.victories*3+a.draws) as score --calculating score
from (
	select name as name, 
	(select count(*) from matches as m
		where (t.id = m.team_1 and m.team_1_goals > m.team_2_goals) or
		      (t.id = m.team_2 and m.team_2_goals > m.team_1_goals)
	) as victories, -- Selecting victories
	(select count(*) from matches as m
		where (t.id = m.team_1 and m.team_1_goals < m.team_2_goals) or
		      (t.id = m.team_2 and m.team_2_goals < m.team_1_goals)
	) as defeats,   -- Selecting defeats
	(select count(*) from matches as m
		where (t.id = m.team_1 and m.team_1_goals = m.team_2_goals) or
		      (t.id = m.team_2 and m.team_2_goals = m.team_1_goals)
	) as draws, -- Selecting draws
	count(*) as matches -- Counting line of games by team
	from teams as t
	inner join matches as m on (t.id = m.team_1 or t.id = m.team_2)
	group by t.id
     ) as a
order by score desc,name; -- Order by desc
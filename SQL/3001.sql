/**
 * Escreva a sua solução aqui
 * Code your solution here
 * Escriba su solución aquí
 */
select p.name,
	CASE WHEN p.type = 'A' THEN 20.0
	     WHEN p.type = 'B' THEN 70.0
	     WHEN p.type = 'C' THEN 530.5
	END
from products as p
order by p.type,p.id desc;
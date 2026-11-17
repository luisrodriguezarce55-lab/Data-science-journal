 -- ¿Cuál es el total vendido por sucursal? ---Equivocado
select sucursal_texto as Sucursal , sum(cantidad) as 'Cantidad de ventas' 
from raw_ventas_pos
where sucursal_texto is not null
 group by sucursal_texto;

 -- ¿Cuáles son los 5 productos más vendidos en unidades?--Equivocado
select top 5 producto_texto as 'Producto vendidos' , sum(cantidad) as 'Cantidad' 
from raw_ventas_pos
 group by producto_texto
 order by cantidad desc;

 -- ¿Cuál es el total vendido por sucursal?
SELECT 
    s.nombre AS sucursal,
    SUM(h.total) AS total_vendido
FROM Hechos_Ventas h
JOIN Dim_Sucursal s 
    ON h.sucursal_id = s.sucursal_id
GROUP BY s.nombre
ORDER BY total_vendido DESC;
GO

-- ¿Cuáles son los 5 productos más vendidos en unidades?
SELECT TOP 5
    p.nombre_producto,
    SUM(h.cantidad) AS unidades_vendidas
FROM Hechos_Ventas h
INNER JOIN Dim_Producto p 
    ON h.producto_id = p.producto_id
GROUP BY p.nombre_producto
ORDER BY unidades_vendidas DESC;
GO

-- ¿Cual es el ticket promedio segun el tipo de cliente?

select
case
	when h.cliente_id is null then 'Sin identificar (walk-in)'
	when c.es_frecuente = 1 then 'Cliente frecuente'
	else 'Cliente no frecuente'
	end as segmento,
	round(avg(h.total), 0) as ticket_promedio,
	count(*) as num_ventas
from hechos_ventas h
	left join dim_cliente c
on h.cliente_id = c.cliente_id
group by
case
	when h.cliente_id is null then 'Sin identificar (walk-in)'
	when c.es_frecuente = 1 then 'Cliente frecuente'
else 'Cliente no frecuente'
end
	order by ticket_promedio desc;

-- ¿Como varian las ventas segun el dia de la semana?

select t.dia_semana, 
	count(*) as num_ventas, 
	sum(h.total) as total_vendido 
from Hechos_Ventas h
 join Dim_Tiempo t
	on h.fecha_id= t.fecha_id
	group by t.dia_semana
	order by total_vendido desc
	-- ¿Qué categoría de producto genera más ingresos?
select top 1 
    cat.nombre as categoria, 
    sum(h.total) as ingresos_totales
from hechos_ventas h
join dim_producto p 
    on h.producto_id = p.producto_id
join dim_categoria cat 
    on p.categoria_id = cat.categoria_id
group by cat.nombre
order by ingresos_totales desc;

--Cuantas ventas de mostrados (sin cliente) hay por sucursal

select 
    s.nombre as sucursal,
    count(*) as ventas_sin_cliente
from hechos_ventas h
join dim_sucursal s 
    on h.sucursal_id = s.sucursal_id
where h.cliente_id is null
group by s.nombre
order by ventas_sin_cliente desc;

--¿Quiénes son los 3 clientes frecuentes que más han gastado?

select top 3
    c.nombre,
    sum(h.total) AS total_gastado,
    count(*) AS num_compras
from hechos_ventas h
join dim_cliente c 
    on h.cliente_id = c.cliente_id
where c.es_frecuente = 1
group by c.nombre
order by total_gastado Desc;
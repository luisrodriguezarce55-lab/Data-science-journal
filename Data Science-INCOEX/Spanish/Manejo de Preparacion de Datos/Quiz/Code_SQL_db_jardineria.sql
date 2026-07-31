use db_jardineria 
go

Select * from cliente
go

select * from cliente
where nombre_contacto ='Jose';

--- comand for searching a name <> diferent a ----
select * from cliente
where nombre_contacto <>'Jose';

--- comand for searching a name = equal a ----
select nombre_contacto from cliente
where nombre_cliente = 'Lasas S.A.';

--- % that apper any where---
select nombre_contacto from cliente
where nombre_contacto like '%luis%';
go

--- % que terminen en %an  que termine---
select nombre_contacto from cliente
where nombre_contacto like '%an';

--- % que terminen en %an  que empiece---
select nombre_contacto from cliente
where nombre_contacto like 'an%';

---Ejemplos---

select nombre_contacto, apellido_contacto, telefono from cliente
where nombre_contacto like 'Ju%';

select nombre_contacto, apellido_contacto, telefono from cliente
where nombre_contacto like '%a';

--- > Limit mayor or less
--- nombre del cont = XXX y AND > 30000

select * from cliente 
where limite_credito >= 30000;

--- > Limit mayor or less
--- nombre del cont = XXX y AND > 10000

select * from cliente 
where nombre_contacto = 'Anne' and limite_credito> 18;

--- operador logico AND (y) ---
--- wn la ciudad que buscan conte lo 
select * from cliente 
where limite_credito > 3000 and ciudad like '%lo%';

--- cialquier ciudad OR

select * from cliente 
where limite_credito > 3000 or ciudad like 'Miami';

---algun espacio en null---
select* from cliente 
where linea_direccion2 is null;

---algun espacio en null---
select* from cliente 
where linea_direccion2 is not null;

select* from cliente 
where not ciudad = 'San Francisco';

--- seleccioname toda la tabla cliente donde la ciudad (diga in) between miami y madrid y numero de representante de ventas sea de 5 y 8, el nombre el numero del cliente empieza con una d
select * from cliente
where ciudad in ('Miami', 'Madrid')
and codigo_empleado_rep_ventas between 5 and 8
and nombre_cliente like 'd%';
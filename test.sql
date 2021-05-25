select count(*) from Track;
select count(*) from Artist;

select * from Album limit 5;
select Title, Name from Album
    join Artist on Album.ArtistID  limit 5;

desc Genre;

-- insert into Genre (name) values ('Trad');

-- select
select last_insert_id();

select * from Genre where GenreID = 27;
select Name from Genre where GenreID = 28;

update Genre SET Name = 'Traditional' where Name = 'Trad';
select Name from Genre where GenreID = 27;

--where
delete from Genre where Name = 'Traditional';

--join
select Name, Title, ArtistID from Track
inner join Album on Track.AlbumID = Album.AlbumID;

select Name as Track, Title as Album, ArtistId from Track
inner join Album on Track.AlbumID = Album.AlbumID;

select Track.Name as Track, Title as Album, Album.ArtistId, Artist.Name as Artist from Track
inner join Album on Track.AlbumID = Album.AlbumID
inner join Artist on Album.ArtistId = Artist.ArtistId
where Artist.Name = 'U2' and Track.Name = 'Pride (In The Name Of Love)';

select Track.Name as Track, Title as Album, Artist.Name as Artist From Track
inner join Album on Track.AlbumID = Album.AlbumID
inner join Artist on Album.ArtistId = Artist.ArtistId
where Track.Name = 'Believe';

--order by
select * from Album
order by Title desc;

select Track.Name, Album.Title from Track
inner join Album on Track.AlbumID = Album.AlbumID
order by Album.Title, Track.Name;

select InvoiceDate, BillingCity, Total from Invoice
order by Total desc
limit 5;

--count
select count(FirstName) from Customer
where FirstName = 'Frank';

--min
select min(LastName) from Customer;
select * from Customer where LastName = 'Almeida';

--max
select max(LastName) from Customer;

--avg
select avg(Total) from Invoice;

--round
select round(avg(total), 2) from Invoice;

--sum
select sum(UnitPrice * Quantity) from InvoiceLine
where InvoiceID = 2;

--group by
select AlbumID, count(*) from Track
group by AlbumID;

select Album.Title, count(*) from Track
inner join Album on Track.AlbumID = Album.AlbumID
group by Track.AlbumID;

select AlbumID, min(UnitPrice) from Track
group by AlbumID;

select AlbumID, round(sum(UnitPrice), 2) from Track
group by AlbumID;

select Album.Title, round(sum(UnitPrice), 2) from Track
inner join Album on Track.AlbumID = Album.AlbumID
group by Track.AlbumID;

--insert
insert into MediaType (Name)
values ('Test Media Type 1');

insert into Album (Title, ArtistId)
values ('Boy', 150);

select AlbumId from Album where Title = 'Boy';

select MediaTypeId from MediaType where Name = 'Protected AAC audio file';

select GenreID from Genre where Name = 'Rock';

insert into Track (Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice)
values ("I Will Follow", 348, 2, 1, 'U2', 220000, 1234, 0.99);
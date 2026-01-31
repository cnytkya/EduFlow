TRUNCATE TABLE attendance; --attendance tablosundaki tüm kayýtlarý sýfýrlar
TRUNCATE TABLE students;
DELETE FROM students; --students tablosundaki kayýtlarý loglayarak siler. bundan dolayý sanki kayýtlar silinmemiþ gibi olur, çünkü logda kalýyor kayýtlar. TRUNCATE kadar sert deðildir.
DBCC CHECKIDENT ('students', RESEED, 0) -- students tablosunda silinen tüm kayýtlarýn id'sini sýfýrlar. log kalýntýsýný önemsemez.
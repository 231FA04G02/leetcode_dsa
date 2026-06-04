-- SELECT
--     p.firstName,
--     p.lastName,
--     a.city,
--     a.state
-- FROM Person p
-- LEFT JOIN Address a
-- ON p.personId = a.personId;

select p.firstName,p.lastName,a.city,a.state from Person as p
left join Address as a on p.personId=a.personId;

CREATE TABLE public.TitanicPassengers (
  id       SERIAL PRIMARY KEY,

  title    VARCHAR(10),
  fname    VARCHAR(30),
  lname    VARCHAR(30),
  ticket_class    VARCHAR(10),
  sex      VARCHAR(10),
  siblings_spouse integer,
  parents_children integer,
  fare integer,
  age integer,
  port    VARCHAR(10),
  cabin   VARCHAR(10),
  probability float,
  survival integer
);



ALTER TABLE public.TitanicPassengers
    OWNER to root;

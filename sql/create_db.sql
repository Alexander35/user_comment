SET client_encoding = 'UTF8';

create database magnit_1;
alter database magnit_1 owner to alexander;

\c magnit_1;

create table region (
    name character varying(100) 
);

ALTER TABLE region ADD COLUMN id BIGSERIAL PRIMARY KEY;

create table town(
    name character varying(100),
    region integer references region(id)
);

ALTER TABLE town ADD COLUMN id BIGSERIAL PRIMARY KEY;

create table comment_stat (
	region integer references region(id),
	town integer references town(id),
	comment_num integer not null		
);

ALTER TABLE comment_stat ADD COLUMN id BIGSERIAL PRIMARY KEY;

create table comment (
	user_name character varying(100),
	user_family_name character varying(100),
	email character varying(100),
	region integer references region(id),
	town integer references town(id),
	patronomic character varying(100),
	phone character varying(100),
	comment character varying(1000),
	visibility boolean,

	created_at timestamp with time zone,
    updated_at timestamp with time zone

);

ALTER TABLE comment ADD COLUMN id BIGSERIAL PRIMARY KEY;

alter table region owner to alexander;
alter table town owner to alexander;
alter table comment_stat owner to alexander;
alter table comment owner to alexander;
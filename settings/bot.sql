create schema botgrandejogos;

create table pnts(
	id_pontos int not null auto_increment,
    nome varchar(100) not null,
    pontos int not null default 0,
    primary key (id_pontos)
);
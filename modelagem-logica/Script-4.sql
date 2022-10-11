CREATE TABLE usuario (
  id serial,
  nome VARCHAR(45) NOT NULL,
  constraint pk_usuario primary key (id));
 
insert into usuario values
(default, 'Esdras Santos'),
(default, 'Layslla Mynlle');

select * from usuario u;


CREATE TABLE receita (
  id serial,
  descricao VARCHAR(60) NOT null,
  tipo CHAR(1) NOT NULL,
  usuario_id INT NOT NULL,
  valor FLOAT NOT NULL,
  data_prevista DATE NOT NULL,
  data_realizada DATE,
  data_criacao DATE NOT null,
  atualizado_em timestamp NOT null,
  constraint pk_receita primary key (id),
  constraint fk_receita_usuario FOREIGN KEY (usuario_id) REFERENCES usuario (id) ON DELETE NO action);
comment on column receita.descricao is 'Recebe a descrição da origem da receita';
comment on column receita.tipo is 'Recebe F para receita FIXA e V para receita VARIÁVEL';
comment on column receita.data_prevista is 'Data em que o valor ficou disponível em saldo corrente';
comment on column receita.data_realizada is 'Data em que o valor foi disponibilzado de forma líquida';
comment on column receita.data_criacao is 'Data em que a receita foi estipulada';
comment on column receita.atualizado_em is 'Recebe atualização a cada nova alteração nos dados';


insert into receita values
(default, 'Salário', 'F', 1, 2539.0, '2022-11-05',null, current_date, now());


CREATE TABLE despesa (
  id serial,
  tipo CHAR(1) NOT NULL,
  descricao VARCHAR(60) NOT NULL,
  valor FLOAT NOT NULL,
  data_criacao DATE NOT null default current_date,
  data_prevista DATE NOT NULL,
  data_pagamento DATE,
  atualizado_em timestamp NOT null default now(),
  nivel_prioridade SMALLINT NOT NULL,
  categoria_despesa_id INT NOT NULL,
  usuario_id INT NOT NULL,
  forma_pgto CHAR(1) NOT null,
  categoria VARCHAR(45) NOT NULL,
  constraint pk_despesa PRIMARY KEY (id),
  CONSTRAINT fk_despesa_usuario FOREIGN KEY (usuario_id) REFERENCES usuario (id) ON DELETE NO action ON UPDATE NO ACTION);
comment on column despesa.tipo is 'Deve receber se a uma despesa é fixa ou recorrente. sendo para fizo e para recorrente.';
comment on column despesa.nivel_prioridade is 'recebe valores entre 1 e 3 onde quanto maior, mais importante.';
comment on column despesa.forma_pgto is 'Recebe para pagamento no cartão de crédito e para pagamento com saldo bancario independente da forma (Ex: pix, ted, doc, saque).';


CREATE TABLE poupanca (
  id serial,
  banco VARCHAR(20) NOT NULL,
  saldo FLOAT NOT NULL,
  usuario_id INT NOT NULL,
  constraint pk_poupanca primary key (id),
  CONSTRAINT fk_poupanca_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES usuario (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
 comment on column poupanca.banco is 'Deve receber o nome do banco';


create table cartao_credito (
  id serial,
  usuario_id INT NOT NULL,
  nome VARCHAR(45) NOT NULL,
  limite_cadastrado FLOAT NOT NULL,
  limite_disponivel FLOAT NOT NULL,
  vencimento_fatura DATE NOT NULL,
  vencimento_cartao DATE,
  constraint pk_cartao_credito PRIMARY KEY (id),
  CONSTRAINT fk_cartao_credito_usuario FOREIGN KEY (usuario_id) references usuario (id) ON DELETE NO action ON UPDATE NO ACTION);
comment on column cartao_credito.nome is 'COMMENT recebe o nome do caertão (Ex: Nubank)';


CREATE TABLE extrato_bancario (
  id serial,
  valor float not null,
  tipo char(3) not null,
  data_transacao date not null,
  instituicao varchar(45) not null,
  agendado bool not null,
  usuario_id int not null,
  constraint pk_extrato_bancario primary key (id),
  constraint fk_extrato_bancario_usuario foreign key (usuario_id) references usuario(id) on delete no action on update no action);

 comment on column extrato_bancario.tipo is 'Parametros:PAG: Pagamentos de títulos DEB: Compra a débito PIX: Transferencias (incluindo ted e doc) APL: Aplicações e Poupança REC: Entrada de Receita RES: Resgate de aplicação';
comment on column extrato_bancario.instituicao is 'Recebe o nome do banco';



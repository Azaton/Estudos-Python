-- criação de banco de ados para o cenário de E-commerce

create database dbEcommerce;
use dbEcommerce;

-- criar tabela cliente

create table client(
	idCliente int auto_increment primary key,
    Fname varchar (1),
    Minit char(3),
    Lname varchar(20),
    CPF char(11) not null,
    constraint unique_cpf_client unique (CPF)
);

-- criar tabela produto
create table product(
	idProduct int auto_increment primary key,
    Pname varchar (1),
    classification_kids bool default false,
    category enum('Eletrônico','Roupas','Brinquedos','Alimentos','Livros') not null, 
    avaliação float default 0,
    size varchar(10)
);

-- criar tabela pedido
create table orders(
	idOrder int auto_increment primary key,
    idOrderClient int,
    orderStatus enum('Cancelado','Confirmado','Em processamento') default 'Em processamento',
    orderDescription varchar(255),
    sendValue float default 10,
    paymentCash bool default false,
    constraint fk_orders_client foreign key (idOrderClient) references client(idCliente)
);
desc orders;

-- criar tabela pagamentos
-- Para ser continuado no desafio: implementar a tabela payments, criando conexão com as tabelas necessárias
-- Atualizar o Schema ER Diagram

create table payments(
	idClient int,
    id_payment int,
	typePayment enum('Boleto','Cartão','Dois Cartões'),
    limitAvailable float,
    primary key(idClient, id_payment)
);

-- criar tabela estoque
create table stock(
	idStock int auto_increment primary key,
    stockLocation varchar(255),
    quantity int default 0
);

-- criar tabela fornecedor
create table supplier(
	idSupplier int auto_increment primary key,
    SocoalName varchar(255) not null,
    CNPJ char(15) not null,
    contact char(11) not null,
    constraint unique_supplier unique (CNPJ)
);
desc supplier;

-- criar tabela vendedor
create table seller(
	idSeller int auto_increment primary key,
    SocialName varchar (255),
    AbstName varchar(255),
	CNPJ char(15),
    CPF char(9),
    location varchar(255),
    contact char(11) not null,
    constraint unique_cnpj_seller unique (CNPJ),
    constraint unique_cpf_seller unique (CPF)
);

-- criar tabela produto do vendedor
create table productSeller(
	idPSeller int,
    idProduct int,
    prodQuantity int default 1,
    primary key (idPSeller, idProduct),
    constraint fk_product_seller foreign key (idPSeller) references seller(idSeller),
    constraint  fk_product_product foreign key (idProduct) references product(idProduct)
);
desc productSeller;

-- criar tabela productOrder
create table productOrder(
	idPOproduct int,
	idPOorder int,
    poQuantity int default 1,
    poStatus enum('Disponível','Sem estoque') default 'Disponível',
    primary key (idPOproduct, idPOorder),
    constraint fk_productorder_seller foreign key (idPOproduct) references product(idProduct),
    constraint fk_productorder_product foreign key (idPOorder) references orders(idOrder)
);
desc productOrder;

-- criar tabela storagelocation
create table storageLocation(
	idLproduct int,
	idLstorage int,
    location varchar(255) not null,
    primary key (idLproduct, idLstorage),
    constraint fk_storage_location_product foreign key (idLproduct) references product(idProduct),
    constraint fk_storage_location_storage foreign key (idLstorage) references stock(idStock)
);

-- criar tabela productSuppliers
create table productSupplier(
	idPsSupplier int,
    idPsProduct int,
    quantity int not null,
    primary key (idPsSupplier, idPsProduct),
    constraint fk_product_supplier_supplier foreign key (idPsSupplier) references supplier(idSupplier),
    constraint fk_product_supplier_product foreign key (idPsProduct) references product(idProduct)
);    
    
show tables;

show databases;
use information_schema;
desc table_constraints;
desc referential_constraints;
select * from referential_constraints;

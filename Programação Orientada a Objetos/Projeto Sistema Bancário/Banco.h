#ifndef BANCO_H
#define BANCO_H

#include <iostream>

#include <string>
using std::string;

#include "PessoaJuridica.h"
#include "PessoaFisica.h"
#include "Pessoa.h"
#include "Conta.h"
#include "ContaCorrente.h"
#include "ContaLimite.h"
#include "ContaPoupanca.h"

//Atualizar, conferir a lógica e finalizar 
class Banco : public PessoaJuridica
{
public:
  Banco(string nomeBanco, Pessoa listacorrentistas, Contas listacontas) : PessoaJuridica(nomeBanco), listacorrentistas(listacorrentistas), listacontas(listacontas) {}
  
  
protected:
  string nomeBanco;
  Pessoa listacorrentistas[];
  Contas listacontas[];

};

#endif

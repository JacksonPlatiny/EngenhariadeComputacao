#ifndef PESSOAJURIDICA_H
#define PESSOAJURIDICA_H

#include "Pessoa.h"

#include <iostream>
using std::cout;
using std::endl;

#include <string>
using std::string;

class PessoaJuridica : public Pessoa
{
public:
  PessoaJuridica(string razaoSocial, string cnpj) : Pessoa(nome), razaoSocial(razaoSocial), cnpj(cnpj) {}

  virtual void ExibirDados() {
    cout << "Dados do cliente: " << endl;
    cout << "Tipo: Pessoa Jurídica" <<endl;
    cout << "Nome Fantasia: " << nomeFantasia << endl;
    cout << "CNPJ: " << cnpj << endl;
    cout << "Razão Social: " << razaoSocial << endl;
  }

private:
  string razaoSocial;
  string cnpj;
};

#endif
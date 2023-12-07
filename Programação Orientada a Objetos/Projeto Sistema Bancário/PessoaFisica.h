#ifndef PESSOAFISICA_H
#define PESSOAFISICA_H

#include "Pessoa.h"

#include <iostream>
using std::cout;
using std::endl;

#include <string>
using std::string;

class PessoaFisica : public Pessoa
{
public:
  PessoaFisica(string cpf) : Pessoa(nome), cpf(cpf) {}

  virtual void ExibirDados() {
    cout << "Dados do cliente: " << endl;
    cout << "Tipo: Pessoa Física" <<endl;
    cout << "Nome: " << nome << endl;
    cout << "CPF: " << cpf << endl;
  }

private:
  string cpf;
};

#endif
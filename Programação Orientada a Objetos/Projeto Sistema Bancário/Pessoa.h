#ifndef PESSOA_H
#define PESSOA_H 

#include <string>
using std::string;

//classe abstrata

class Pessoa
{
public:
  Pessoa(string nome) : nome(nome) { }

  //metodo virtual puro
  virtual void exibirDados() = 0;

private:
  string nome;
};

#endif
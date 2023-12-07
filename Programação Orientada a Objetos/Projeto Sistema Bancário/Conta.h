#ifndef CONTA_H
#define CONTA_H

#include <iostream>

#include <string>
using std::string;

#include "Pessoa.h"
#include "Excecao.h"

class Conta {
public:
  Conta(int conta, string nome, double saldo = 0.0): conta(conta),Pessoa(nome),saldo(saldo) { tTransacoes = 0; }
  
  virtual ~Conta() {}
  
  bool &operator<<(const Conta & a)
{
    OPERACAO operacao = {data, valor, descricao};
    a.op[tTransacoes++] = operacao;
    a.saldo += a.valor;

  return true;
}

  virtual bool &operator>>(const Conta & a)
{
    {
    if (a.valor > a.saldo){
      throw SaldoInsuficiente();
      return false;}

    OPERACAO operacao = {data, valor, descricao};
    a.op[tTransacoes++] = operacao;
    a.saldo -= a.valor;

    return true;
  }
}

  virtual void extrato() = 0;

protected:
  int conta;
  Pessoa nome*;
  double saldo;


  struct OPERACAO {
    string data;
    double valor;
    string descricao;
  };

  OPERACAO op[30];
  int tTransacoes;

};

#endif
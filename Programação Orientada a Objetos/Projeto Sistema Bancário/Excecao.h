#ifndef EXCECAO_H
#define EXCECAO_H

#include <stdexcept>

class ExcedeLimite : public std::runtime_error
{
public:
  ExcedeLimite(const char *e= "O valor digitado excede o limite de saldo/transferencia possível para esta conta."): runtime_error(e) {}
};

class SaldoInsuficiente : public std::runtime_error
{
public:
  SaldoInsuficiente(const char *e= "Saldo da conta insuficiente para continuar a operação com o valor solicitado."): runtime_error(e) {}
};

class ContaNaoEncontrada : public std::runtime_error
{
public:
  ContaNaoEncontrada(const char *e = "Esse número de conta fornecido não está em nosso banco de dados. Confira e tente novamente."): runtime_error(e) {}
};


#endif

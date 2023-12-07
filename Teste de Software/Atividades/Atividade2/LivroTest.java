package Atividade2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class LivroTest {

    @Test
    public void testVerificaLancamento_EdicaoMaiorQue2022() {
        Livro livro = new Livro("Livro de Teste", 2023, "Autor de Teste", "ISBN12345");
        assertTrue(livro.verificaLancamento());
    }

    @Test
    public void testVerificaLancamento_EdicaoIgualA2022() {
        Livro livro = new Livro("Livro de Teste", 2022, "Autor de Teste", "ISBN12345");
        assertFalse(livro.verificaLancamento());
    }

    @Test
    public void testVerificaLancamento_EdicaoMenorQue2022() {
        Livro livro = new Livro("Livro de Teste", 2021, "Autor de Teste", "ISBN12345");
        assertFalse(livro.verificaLancamento());
    }

    @Test
    public void testGetNome() {
        Livro livro = new Livro("Livro de Teste", 2023, "Autor de Teste", "ISBN12345");
        assertEquals("Livro de Teste", livro.getNome());
    }

    @Test
    public void testSetNome() {
        Livro livro = new Livro("Livro Antigo", 2023, "Autor de Teste", "ISBN12345");
        livro.setNome("Livro Novo");
        assertEquals("Livro Novo", livro.getNome());
    }
    
    @Test
    public void testGetEdicao() {
        Livro livro = new Livro("Livro de Teste", 2023, "Autor de Teste", "ISBN12345");
        assertEquals(2023, livro.getEdicao());
    }

    @Test
    public void testSetEdicao() {
        Livro livro = new Livro("Livro Antigo", 2023, "Autor de Teste", "ISBN12345");
        livro.setEdicao(2025);
        assertEquals(2025, livro.getEdicao());
    }
    
    @Test
    public void testGetAutor() {
        Livro livro = new Livro("Livro de Teste", 2023, "Autor de Teste", "ISBN12345");
        assertEquals("Autor de Teste", livro.getAutor());
    }

    @Test
    public void testSetAutor() {
        Livro livro = new Livro("Livro Antigo", 2023, "Autor de Teste", "ISBN12345");
        livro.setAutor("Autor Novo");
        assertEquals("Autor Novo", livro.getAutor());
    }

    @Test
    public void testGetISBN() {
        Livro livro = new Livro("Livro de Teste", 2023, "Autor de Teste", "ISBN12345");
        assertEquals("ISBN12345", livro.getISBN());
    }

    @Test
    public void testSetISBN() {
        Livro livro = new Livro("Livro Antigo", 2023, "Autor de Teste", "ISBN12345");
        livro.setISBN("ISBN54321");
        assertEquals("ISBN54321", livro.getISBN());
    }
}

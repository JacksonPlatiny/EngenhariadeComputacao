package Atividade1;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class ProvaTest {
	@Test
	public void testVetor() {
		int [] vet = {89, 90, 84, 91};
		int r = Prova.vetor(vet.length, vet);
		assertEquals(91, r);
	}
	

}

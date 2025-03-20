package Capitulo3;
public class InvoiceTest {
    public static void main(String[] args){
        Invoice invoice = new Invoice();
        System.out.println(invoice.getInvoiceAmount(5.5, 4));
        invoice.setDescricao("PUTA RAARA");
        System.out.println(invoice.getDescricao());
    }
}
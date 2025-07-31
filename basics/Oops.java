class Data
{
    int GetData(int a, int b) {
        return a + b;
    }
    

}
public class Oops {
    public static void main(String[] args) {
        Data obj = new Data();
        obj.GetData(12,4);
        System.out.println("value"+obj.GetData(12,4));
        

    }
}

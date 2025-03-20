package Capitulo3;
public class IMC {
    private float weight, height;

    public void setWeight(float weight){
        this.weight = weight;
    }
    public float getWeight(){
        return weight;
    }
    public void setHeight(float height){
        this.height = height;
    }
    public float getHeight(){
        return height;
    }

    public float imcCalcu(){
        return weight/(float) Math.pow(height, 2.0);
    }
    
}

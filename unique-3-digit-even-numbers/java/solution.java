import java.util.ArrayList;
import java.util.List;


class Solution {
    public int totalNumbers(int[] digits) {
        List<Integer> list_solution = new ArrayList<Integer>();
        int temp_value;
        for (int i=0; i < digits.length; i++){
            if (digits[i] != 0){
                for(int j=0;j < digits.length;j++){
                    if (j!=i){
                        for(int k = 0; k < digits.length; k++ ){
                            if (k != j && k != i){
                                temp_value = digits[i] *100 + digits[j] * 10 + digits[k];
                                //test value
                                if (temp_value % 2 == 0){
                                    list_solution.add(temp_value);
                                }
                            }
                        }
                    }
                }
            }

        }

        // count number of unique element 
        System.out.println(list_solution);
        if(list_solution.size()>0){
            int unique_element = 1; //begin with 1 because we do not check last element of the array
            for(int i = 0; i < list_solution.size() -1 ; ++i){
                int current_value = list_solution.get(i);
                int found_copy = 0;
                for (int j = i +1; j < list_solution.size(); ++j){
                    int value = list_solution.get(j);
                    if(value == current_value){
                        found_copy = 1;
                        break;
                    }
                }
                if(found_copy == 0){
                    ++unique_element;
                }
            }
            return unique_element;
        }
        else{
            return 0;
        }

    }

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(a.totalNumbers(new int[]{1, 2, 3,4}));
    }
}

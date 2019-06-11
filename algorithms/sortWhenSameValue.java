import java.util.HashMap;
import java.util.ArrayList;
import java.util.Map.Entry;
import java.util.stream.Collectors;
import java.util.Comparator;
import java.util.Collections;

class sortWhenSameValue{

public static void main(String [] args){

HashMap<Holder, Double> map = new HashMap<>();

map.put(new Holder(1,0), 3.0);
map.put(new Holder(1,2), 1.0);
map.put(new Holder(0,0), 5.0);
map.put(new Holder(1,1), 2.0);
map.put(new Holder(0,1), 4.0);

ArrayList<Entry<Holder, Double>> entries = new ArrayList<Entry<Holder, Double>>(map.entrySet());
System.out.println(entries);

Collections.sort(entries, new Comparator<Entry<Holder, Double>>(){
	@Override
	public int compare(Entry<Holder, Double> arg0, Entry<Holder, Double> arg1){
		return arg1.getValue().compareTo(arg0.getValue());
	}

});

System.out.println(entries);
}



}

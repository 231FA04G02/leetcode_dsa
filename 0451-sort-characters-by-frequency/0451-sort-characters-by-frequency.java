class Solution {
    public String frequencySort(String s) {
         Map<Character, Integer> freqMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }
        List<Map.Entry<Character, Integer>> list = new ArrayList<>(freqMap.entrySet());
        list.sort((a, b) -> b.getValue() - a.getValue());

       
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<Character, Integer> entry : list) {
            char c = entry.getKey();
            int freq = entry.getValue();
            sb.append(String.valueOf(c).repeat(freq)); 
        }

        return sb.toString();
    }
}
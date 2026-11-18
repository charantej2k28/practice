import java.util.*;

class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> set = new HashSet<>(wordDict);
        Map<Integer, List<String>> memo = new HashMap<>();

        return dfs(s, 0, set, memo);
    }

    private List<String> dfs(String s, int start, Set<String> set,
                             Map<Integer, List<String>> memo) {
        if (memo.containsKey(start)) {
            return memo.get(start);
        }

        List<String> result = new ArrayList<>();

        if (start == s.length()) {
            result.add("");
            return result;
        }

        for (int end = start + 1; end <= s.length(); end++) {
            String word = s.substring(start, end);

            if (set.contains(word)) {
                List<String> sub = dfs(s, end, set, memo);

                for (String sentence : sub) {
                    if (sentence.isEmpty()) {
                        result.add(word);
                    } else {
                        result.add(word + " " + sentence);
                    }
                }
            }
        }

        memo.put(start, result);
        return result;
    }
}
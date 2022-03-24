package com.amdocs.RecursiveResolutionHackathon.Service;

import com.amdocs.RecursiveResolutionHackathon.Resources.Case;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Service;
import org.springframework.util.ResourceUtils;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class QueryHandler {

    Map<String,Case> cases = new HashMap<>();


    public QueryHandler() {
//        Map<String,Case> initialCases = new HashMap<>();
//        Case case1 = new Case("1","caseLwcwl1");
//        Case case2 = new Case("2", "caseLevel2");
//        initialCases.put("1",case1);
//        initialCases.put("2",case2);
//
//        this.cases = initialCases;

        ObjectMapper mapper = new ObjectMapper();
        try {
             String path = "src/test/resources/caseJson.json";


            final File file = ResourceUtils.getFile(path);
           List<Case> cases = mapper.readValue(file,new TypeReference<List<Case>>(){});

           for(Case c :cases )  {
               this.cases.put(c.getId(),c);
           }

        }catch (IOException ex) {
            ex.printStackTrace();
        }

    }

    public Case getCaseById(String id) {

        return this.cases.get(id);
    }

    public Case updateCaseById(String id, Case updatedCase) {
        cases.put(id,updatedCase);
        return cases.get(id);
    }

    public List<Case> getCases() {
        ArrayList<Case> res = new ArrayList<>();
        for(Map.Entry<String, Case> entry : this.cases.entrySet()) {
            res.add(entry.getValue());
        }

        return res;
    }

    public void setCases(Map<String, Case> cases) {
        this.cases = cases;
    }

    public void setCase(String id, Case inputCase) {
        this.cases.put(id,inputCase);
    }
}

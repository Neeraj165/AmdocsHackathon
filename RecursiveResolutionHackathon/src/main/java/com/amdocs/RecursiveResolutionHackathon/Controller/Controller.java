package com.amdocs.RecursiveResolutionHackathon.Controller;


import com.amdocs.RecursiveResolutionHackathon.Resources.Case;
import com.amdocs.RecursiveResolutionHackathon.Service.QueryHandler;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@RestController
public class Controller {

    @Autowired
    QueryHandler queryHandler;

//  @GetMapping(path ="/performAction/{caseId}")
  public Object handleRequestPost(@PathVariable String caseId) {
//
//        //Case firstCase = new Case("3","thiredleel");
//        //queryHandler.setCase("3",firstCase);
//
//       // return queryHandler.getCases();
//
////        HttpHeaders headers = new HttpHeaders();
////        headers.setContentType(MediaType.APPLICATION_JSON);
////        HttpEntity requestToBackend = new HttpEntity("http://10.80.222.51:5000/getCustomerList",headers);
////
////        RestTemplate restTemplate = new RestTemplate();
////        Object response = restTemplate.postForObject("http://10.80.222.51:5000/getResolutionAction",requestToBackend,Object.class);
////
////        return response;
//    }

    @GetMapping("/getCaseList")
    public List<Case> getCaseList() {

        return queryHandler.getCases();
    }
}

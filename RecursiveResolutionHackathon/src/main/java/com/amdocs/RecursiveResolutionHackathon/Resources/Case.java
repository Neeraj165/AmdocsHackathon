package com.amdocs.RecursiveResolutionHackathon.Resources;

import java.util.ArrayList;
import java.util.List;

public class Case {

//    public Case(String id, String caseLevel1) {
//        this.id  = id;
//        this.caseLevel1 = caseLevel1;
//    }

    String id;

    String status;

    String caseLevel1;

    String caseLevel2;

    String caseLevel3;

    String caseLevel4;

    String caseLevel5;

    List<Resolution> resolution;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getCaseLevel1() {
        return caseLevel1;
    }

    public void setCaseLevel1(String caseLevel1) {
        this.caseLevel1 = caseLevel1;
    }

    public String getCaseLevel2() {
        return caseLevel2;
    }

    public void setCaseLevel2(String caseLevel2) {
        this.caseLevel2 = caseLevel2;
    }

    public String getCaseLevel3() {
        return caseLevel3;
    }

    public void setCaseLevel3(String caseLevel3) {
        this.caseLevel3 = caseLevel3;
    }

    public String getCaseLevel4() {
        return caseLevel4;
    }

    public void setCaseLevel4(String caseLevel4) {
        this.caseLevel4 = caseLevel4;
    }

    public String getCaseLevel5() {
        return caseLevel5;
    }

    public void setCaseLevel5(String caseLevel5) {
        this.caseLevel5 = caseLevel5;
    }

    public List<Resolution> getResolution() {
        return resolution;
    }

    public void setResolution(List<Resolution> resolution) {
        this.resolution = resolution;
    }





}

package com.nyxvision.intelreporter.repository;

import com.nyxvision.intelreporter.models.IntelReport;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface IntelReportRepository extends CrudRepository<IntelReport,Integer> {
}

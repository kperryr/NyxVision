package com.nyxvision.intelreporter.repository;

import com.nyxvision.intelreporter.models.User;
import org.springframework.data.repository.CrudRepository;

public interface UserRepository extends CrudRepository<User, Integer> {
}

find_package(PkgConfig)

pkg_check_modules(XML libxml-2.0)
pkg_check_modules(SQL sqlite3)


if (XML_FOUND AND SQL_FOUND)
    add_executable(getedges getedges.c)
    add_executable(countnodes countnodes.c)
    add_executable(getmissingandreport getmissingandreport.c)
    add_executable(fillinpostcode fillinpostcode.c)
    add_executable(fillinpostcodepoi fillinpostcodepoi.c)
    add_executable(osmosispolygon osmosispolygon.c)

    install(TARGETS getedges DESTINATION bin)
    install(TARGETS countnodes DESTINATION bin)
    install(TARGETS getmissingandreport DESTINATION bin)
    install(TARGETS fillinpostcode DESTINATION bin)
    install(TARGETS fillinpostcodepoi DESTINATION bin)
    install(TARGETS osmosispolygon DESTINATION bin)

    target_link_libraries(getedges ${XML_LIBRARIES})
    target_link_libraries(countnodes ${XML_LIBRARIES})
    target_link_libraries(getmissingandreport ${XML_LIBRARIES} ${SQL_LIBRARIES})
    target_link_libraries(fillinpostcode ${XML_LIBRARIES} ${SQL_LIBRARIES})
    target_link_libraries(fillinpostcodepoi ${XML_LIBRARIES} ${SQL_LIBRARIES})
    target_link_libraries(osmosispolygon ${XML_LIBRARIES} ${SQL_LIBRARIES})
    include_directories(${XML_INCLUDE_DIRS} ${SQL_INCLUDE_DIRS})
else (XML_FOUND AND SQL_FOUND)
    MESSAGE( "Missing one more packages for building gui. Skipping")
endif(XML_FOUND AND SQL_FOUND)


        ('hgt', 
            thing(lambda)
            .and(
                    thing(
                        thing(lambda).and(
                        thing(lambda)).
                    or(
                    thing(
                        thing(lambda).and(
                        thing(lambda)))
                ))
            And(
                lambda f: bool(re.search("^[0-9]+(in|cm)$", f)),
                Or(
                    And(
                        lambda num, units: 150 <= num  <= 193,
                        lambda num, units: units  == 'cm',
                    ),
                    And(
                        lambda num, units: 59 <= num  <= 76,
                        lambda num, units: units  == 'in',
                    ),
                    pre=lambda f: (int(re.search().group('num')), re.search().group('units'))
                )
            )
        )

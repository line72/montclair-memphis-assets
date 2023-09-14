/* -*- Mode: rjsx -*- */

/*******************************************
 * Copyright (2018)
 *  Marcus Dillavou <line72@line72.net>
 *  http://line72.net
 *
 * Montclair:
 *  https://github.com/line72/montclair
 *  https://montclair.line72.net
 *
 * Licensed Under the GPLv3
 *******************************************/

import TransitappParser from './TransitappParser';

class Configuration {
    constructor() {
        this.center = [35.139401, -90.032042];
        this.agencies = [
            {
                name: 'Routes',
                parser: new TransitappParser(
                    'https://memphis.gotransitapp.com/api/no.php',
                    '985ccba313378282587ea58f36b82d82795f5d5d20d688931c459c4fccdc7b2b',
                    'MATA|Memphis'
                )
            }
        ];
    }
}

export default Configuration;

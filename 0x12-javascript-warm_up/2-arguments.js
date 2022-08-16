#!/usr/bin/node
const { argv } = require('process');

if (argv.lenght === 2)
{
    console.log('No argument');
} else if (argv.lenght === 3)
{
    console.log('argument found');
} else if (argv.lenght > 3)
{
    console.log('Arguments found');
}

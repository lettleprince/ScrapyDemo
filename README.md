# ScrapyDemo

ScrapyDemo is a Scrapy project for the [blog](http://ibloodline.com/articles/2017/12/15/Scrapy-Tutorial.html).It can scrape questions from [stackoverflow](https://stackoverflow.com/questions/tagged/scrapy).

# Extracted data

This project extracts questions and users.The extracted data looks like this sample:

```json
{
    "question_content": "How to pass a user defined argument in scrapy spider",
    "user": "L Lawliet"
}
```

# Spiders

This project contains three spiders and you can list them using the `list` command:

```shell
$ scrapy list
stackoverflow
tag
user
```

# Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

```shell
$ scrapy crawl stackoverflow
```

If you want to save the scraped data to a file, you can pass the `-o` option:

```shell
$ scrapy crawl stackoverflow -o stackoverflow.jl
```